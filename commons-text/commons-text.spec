Name:           commons-text
Version:        1.15.0
Release:        1%{?dist}
Summary:        Apache Commons library for text processing and manipulation

License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-text
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-lang3)

%description
Apache Commons Text is a set of utility functions and reusable components
for the purpose of processing and manipulating text that should be
considered as additions to the standard JDK text handling.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
Group:          Documentation
Packager:       openEuler Builder <builder@openeuler.org>

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

# Remove parent POM (commons-parent not available in openEuler)
%pom_remove_parent

# Inject groupId inherited from commons-parent, and required build properties
%pom_xpath_inject "pom:project" "<groupId>org.apache.commons</groupId>"
%pom_xpath_inject "pom:project/pom:properties" "
  <maven.compiler.source>1.8</maven.compiler.source>
  <maven.compiler.target>1.8</maven.compiler.target>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
"

# Remove plugins not available or not needed in openEuler build environment
%pom_remove_plugin -r :japicmp-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r com.github.spotbugs:spotbugs-maven-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-assembly-plugin
%pom_remove_plugin -r :maven-scm-publish-plugin
%pom_remove_plugin -r :maven-pmd-plugin
%pom_remove_plugin -r :taglist-maven-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 1.15.0-1
- Initial package for commons-text 1.15.0
