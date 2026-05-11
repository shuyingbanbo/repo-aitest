Name:           mapstruct
Version:        1.5.5.Final
Release:        1%{?dist}
Summary:        Annotation processor for generating type-safe bean mappers

License:        Apache-2.0
URL:            https://github.com/mapstruct/mapstruct
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-11-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  freemarker
BuildRequires:  maven-plugin-bundle

%description
MapStruct is a code generator that greatly simplifies the implementation
of mappings between Java bean types based on a convention over
configuration approach. The generated mapping code uses plain method
invocations and thus is fast, type-safe and easy to understand.

%package processor
Summary:        MapStruct annotation processor
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description processor
Annotation processor for MapStruct that generates type-safe bean mapper
implementations at compile time.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
Group:          Documentation
Packager:       openEuler Builder <builder@openeuler.org>

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

# Skip non-core modules first so recursive plugin removal doesn't scan them
%pom_disable_module distribution
%pom_disable_module integrationtest
%pom_disable_module documentation

# Remove release/publish/QA plugins not needed for offline build
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :flatten-maven-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :forbiddenapis
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :japicmp-maven-plugin
%pom_remove_plugin -r :properties-maven-plugin

# Remove test-only BOM imports unavailable offline
%pom_remove_dep -r org.jboss.arquillian:arquillian-bom parent/pom.xml

# gem-api is shaded into the processor jar; mark optional so xmvn skips
# generating a runtime Requires for this unavailable artifact
%pom_xpath_inject "pom:dependency[pom:artifactId='gem-api']" "<optional>true</optional>" processor/pom.xml

# Assign processor module to the processor subpackage
%mvn_package "org.mapstruct:mapstruct-processor" processor

%build
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

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
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 1.5.5.Final-1
- Initial package for mapstruct 1.5.5.Final
