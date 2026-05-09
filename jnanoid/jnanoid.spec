Name:           jnanoid
Version:        1.0.1
Release:        1%{?dist}
Summary:        A unique string ID generator for Java

License:        MIT
URL:            https://github.com/aventrix/jnanoid
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local

Requires:       java-headless >= 1:1.8.0

%description
JNanoId is a unique string ID generator for Java. It provides URL-friendly,
secure, customizable unique IDs using a SecureRandom-based algorithm.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin com.github.ekryd.sortpom:sortpom-maven-plugin

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
* Sat May 09 2026 openEuler Builder <builder@openeuler.org> - 1.0.1-1
- Initial package for jnanoid 1.0.1
