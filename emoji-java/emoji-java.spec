Name:           emoji-java
Version:        5.1.1
Release:        1%{?dist}
Summary:        Emoji library for Java

License:        MIT
URL:            https://github.com/vdurmont/emoji-java
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(org.json:json)

%description
emoji-java is a lightweight Java library for working with emojis. It provides
methods to convert emoji aliases, HTML entities, and Unicode characters, as
well as tools to detect, remove, or extract emojis from text.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
Group:          Documentation
Packager:       openEuler Builder <builder@openeuler.org>

%description javadoc
API documentation for %{name}.

%prep
%autosetup

# Update org.json version to match packaged version
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId='org.json']/pom:version" "20250517"

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md
%doc README.md CHANGELOG.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md

%changelog
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 5.1.1-1
- Initial package for emoji-java 5.1.1
