Name:           zt-zip
Version:        1.17
Release:        1%{?dist}
Summary:        Small and fast library to process ZIP archives

License:        Apache-2.0
URL:            https://github.com/zeroturnaround/zt-zip
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(org.slf4j:slf4j-api)

%description
Small and fast library to create, modify or explode ZIP archives,
either on disk or in memory.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
Group:          Documentation
Packager:       openEuler Builder <builder@openeuler.org>

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-source-plugin

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 1.17-1
- Initial package for zt-zip 1.17
