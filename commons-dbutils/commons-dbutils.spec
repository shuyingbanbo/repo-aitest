Name:           commons-dbutils
Version:        1.8.1
Release:        1%{?dist}
Summary:        Apache Commons library for JDBC helper utilities

License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-dbutils
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local

%description
Apache Commons DbUtils is a small set of classes designed to make working
with JDBC easier. JDBC resource cleanup code is mundane and error-prone, so
these classes abstract out the cleanup work so that developers do not need
to write boilerplate code.

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
# Note: commons-dbutils declares its own groupId, no need to inject it
%pom_remove_parent

# Remove plugins not available or not needed in openEuler build environment
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r com.github.spotbugs:spotbugs-maven-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-assembly-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :maven-changes-plugin
%pom_remove_plugin -r :maven-pmd-plugin

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
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 1.8.1-1
- Initial package for commons-dbutils 1.8.1
