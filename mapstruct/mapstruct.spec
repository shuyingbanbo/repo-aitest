Name:           mapstruct
Version:        1.6.3
Release:        1%{?dist}
Summary:        An annotation processor for generating type-safe bean mappers
BuildArch:      noarch
License:        Apache-2.0
URL:            https://github.com/mapstruct/mapstruct
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

# processor module requires Java 11+ to compile
BuildRequires:  java-11-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(org.freemarker:freemarker)
BuildRequires:  mvn(org.mapstruct.tools.gem:gem-api)
BuildRequires:  mvn(org.mapstruct.tools.gem:gem-processor)

%description
MapStruct is a code generator that greatly simplifies the implementation
of mappings between Java bean types based on a convention over
configuration approach. The generated mapping code uses plain method
invocations and thus is fast, type-safe, and easy to understand.

%package processor
Summary:        MapStruct annotation processor
%description processor
The MapStruct annotation processor generates type-safe bean mapper
implementations from annotated interfaces at compile time.

%package javadoc
Summary:        Javadoc for %{name}
%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

# Disable the deprecated relocation stub (no real sources, no install needed)
%pom_disable_module core-jdk8
# integrationtest requires Arquillian/WildFly containers not available in RPM build
%pom_disable_module integrationtest
# distribution and documentation are packaging/release artifacts not needed for RPM
%pom_disable_module distribution
%pom_disable_module documentation

# Remove arquillian BOM import from dependencyManagement (offline build can't resolve it)
%pom_remove_dep -r org.jboss.arquillian:arquillian-bom parent/pom.xml
%pom_remove_dep -r org.jboss.arquillian.container:arquillian-weld-se-embedded-1.1 parent/pom.xml
%pom_remove_dep -r org.jboss.weld:weld-core-impl parent/pom.xml

# Remove all plugins that are unavailable or cause failures in the offline
# xmvn build environment.  pom_disable_module must come before the -r sweep.
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :forbiddenapis
%pom_remove_plugin -r :japicmp-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
# flatten-maven-plugin is a publish-time POM flattening tool, not needed here
%pom_remove_plugin -r :flatten-maven-plugin
# maven-bundle-plugin generates OSGi MANIFEST; not required for RPM packaging
%pom_remove_plugin -r :maven-bundle-plugin
# maven-dependency-plugin is used only to unpack the freemarker license file;
# the freemarker license is already part of the source tarball, so skip it
%pom_remove_plugin -r :maven-dependency-plugin

# freemarker and gem-api are shaded into the processor jar at package time.
# Marking them optional prevents xmvn from emitting runtime RPM Requires.
%pom_xpath_inject "pom:dependency[pom:artifactId='freemarker']" \
    "<optional>true</optional>" processor/pom.xml
%pom_xpath_inject "pom:dependency[pom:artifactId='gem-api']" \
    "<optional>true</optional>" processor/pom.xml

# jakarta.xml.bind-api 3.0.1 not available in openEuler; dep is optional/provided only
%pom_remove_dep jakarta.xml.bind:jakarta.xml.bind-api processor/pom.xml

# Remove annotationProcessorPaths: Gem classes are pre-generated in %build step 2,
# so maven-compiler-plugin must not re-run gem-processor and recreate them.
%pom_xpath_remove \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:annotationProcessorPaths" \
    processor/pom.xml
# Disable annotation processing during compilation to avoid self-referential processor load
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration" \
    "<compilerArgs><arg>-proc:none</arg></compilerArgs>" \
    processor/pom.xml

# maven-bundle-plugin generated the OSGi MANIFEST.MF that maven-jar-plugin
# references in core/pom.xml.  Since we removed maven-bundle-plugin, we must
# also remove the <archive><manifestFile>…</manifestFile></archive> stanza so
# maven-jar-plugin creates a default manifest instead of failing.
%pom_xpath_remove \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive" \
    core/pom.xml


# Route artifacts to the correct subpackages
%mvn_package ':mapstruct-processor' processor
# build-config contains only checkstyle/IDE config resources; suppress install
%mvn_package ':mapstruct-build-config' __noinstall

# jakarta.xml.bind-api 3.x is not available in openEuler; remove Jakarta JAXB
# sources that depend on it. The javax.xml.bind (JAXB 2.x) path still works.
rm -f processor/src/main/java/org/mapstruct/ap/internal/gem/jakarta/JakartaGemGenerator.java
rm -f processor/src/main/java/org/mapstruct/ap/internal/model/source/selector/JakartaXmlElementDeclSelector.java
rm -f processor/src/main/java/org/mapstruct/ap/internal/processor/JakartaCdiComponentProcessor.java
rm -f processor/src/main/java/org/mapstruct/ap/internal/processor/JakartaComponentProcessor.java
sed -i '/JakartaXmlElementDeclSelector/d' \
  processor/src/main/java/org/mapstruct/ap/internal/model/source/selector/MethodSelectors.java

%build
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk

# Step 1: build only core so its jar is available for gem code generation
xmvn --batch-mode --offline -Dmaven.test.skip=true -DskipDistribution=true \
  --projects parent,build-config,core package

# Step 2: generate Gem helper classes via javac annotation processing.
# Only remove DeprecatedGem.java — the Java 8 version lacks since/forRemoval attributes.
# All other *Gem.java files in the source tree are hand-written enum gems and must stay.
GEM_OUT=%{_builddir}/gem-generated
rm -f processor/src/main/java/org/mapstruct/ap/internal/gem/DeprecatedGem.java
mkdir -p $GEM_OUT
$JAVA_HOME/bin/javac \
  -source 11 -target 11 \
  -proc:only \
  -processorpath /usr/share/java/tools-gem/gem-processor.jar \
  -classpath core/target/mapstruct-%{version}.jar:/usr/share/java/jaxb-api.jar:/usr/share/java/tools-gem/gem-api.jar \
  -s $GEM_OUT \
  processor/src/main/java/org/mapstruct/ap/internal/gem/GemGenerator.java
find $GEM_OUT -name '*.java' | while read f; do
  rel="${f#$GEM_OUT/}"
  install -Dm644 "$f" "processor/src/main/java/$rel"
done

# Step 3: full xmvn build (processor now has all generated Gem classes in source tree)
%mvn_build -f -- -DskipDistribution=true

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc readme.md

%files processor -f .mfiles-processor
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Tue May 19 2026 openEuler Builder <builder@openeuler.org> - 1.6.3-1
- Initial package
