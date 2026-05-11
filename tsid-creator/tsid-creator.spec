Name:           tsid-creator
Version:        5.2.6
Release:        1%{?dist}
Summary:        Java library for generating Time-Sorted Unique Identifiers (TSID)

License:        MIT
URL:            https://github.com/f4b6a3/tsid-creator
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local

%description
tsid-creator is a Java library for generating Time-Sorted Unique Identifiers
(TSID). A TSID is a 64-bit value that encodes a creation time and a random
component, making it suitable for use as a database primary key with good
index locality.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
Group:          Documentation
Packager:       openEuler Builder <builder@openeuler.org>

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

# Remove publishing/signing plugins not needed in openEuler build environment
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md CHANGELOG.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 5.2.6-1
- Initial package for tsid-creator 5.2.6
