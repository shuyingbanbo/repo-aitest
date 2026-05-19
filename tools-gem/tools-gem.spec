Name:           tools-gem
Version:        1.0.0.Alpha3
Release:        1%{?dist}
Summary:        An annotation processor for generating gems for annotations
BuildArch:      noarch
License:        Apache-2.0
URL:            https://github.com/mapstruct/tools-gem
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.freemarker:freemarker)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)

%description
MapStruct Tools Gem provides an annotation processor for generating
type-safe wrappers (gems) for Java annotations. These gems allow
comfortable, type-safe access to annotation attributes and are used
by annotation processors such as MapStruct.

%package -n gem-api
Summary:        MapStruct Tools Gem API

%description -n gem-api
The API module of MapStruct Tools Gem, providing the core annotation
types and interfaces for defining and accessing annotation gems.

%package -n gem-processor
Summary:        MapStruct Tools Gem Processor
Requires:       mvn(org.freemarker:freemarker)

%description -n gem-processor
The annotation processor module of MapStruct Tools Gem. Processes
GemDefinition annotations and generates corresponding Gem classes.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

# Disable the test module (test helper only, not published artifact)
%pom_disable_module test

# Now remove plugins that are not compatible with offline/openEuler build
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :flatten-maven-plugin

# Remove maven-bundle-plugin (OSGi manifest generation not needed for RPM)
# and fix the maven-jar-plugin manifestFile reference in api module
%pom_remove_plugin :maven-bundle-plugin api/pom.xml
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive" "<addMavenDescriptor>false</addMavenDescriptor>" api/pom.xml || true
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive/pom:manifestFile" api/pom.xml || true

# Remove maven-dependency-plugin from processor (used to unpack freemarker license, not available offline)
%pom_remove_plugin :maven-dependency-plugin processor/pom.xml

# Map artifacts to subpackages
%mvn_package ":gem-api" gem-api
%mvn_package ":gem-processor" gem-processor

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files -n gem-api -f .mfiles-gem-api
%license LICENSE.txt

%files -n gem-processor -f .mfiles-gem-processor
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Tue May 19 2026 Java_Bot <Java_Bot@openeuler.org> - 1.0.0.Alpha3-1
- Initial package
