Name:           ulid-creator
Version:        5.2.4
Release:        1%{?dist}
Summary:        Java library for generating ULIDs

License:        MIT
URL:            https://github.com/f4b6a3/ulid-creator
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local

%description
Java library for generating ULIDs (Universally Unique Lexicographically
Sortable Identifiers).

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
%pom_remove_plugin -r :central-publishing-maven-plugin
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
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 5.2.4-1
- Initial package for ulid-creator 5.2.4
