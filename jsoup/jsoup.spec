Name:           jsoup
Version:        1.22.2
Release:        1%{?dist}
Summary:        Java HTML parser for HTML editing, cleaning, scraping, and XSS safety

License:        MIT
URL:            https://jsoup.org
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(org.jspecify:jspecify)

%description
jsoup is a Java library for working with real-world HTML. It provides a
convenient API for fetching URLs and extracting and manipulating data,
using the best of HTML5 DOM methods and CSS selectors. jsoup implements
the WHATWG HTML5 specification and parses HTML to the same DOM as modern
browsers.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
Group:          Documentation
Packager:       openEuler Builder <builder@openeuler.org>

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

# Remove publishing/signing plugins
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :central-publishing-maven-plugin
%pom_remove_plugin -r :maven-source-plugin

# Remove plugins not available in openEuler build environment
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :japicmp-maven-plugin
%pom_remove_plugin -r :maven-failsafe-plugin
%pom_remove_plugin -r org.apache.felix:maven-bundle-plugin

# Remove the manifestFile reference that depended on maven-bundle-plugin output
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:archive/pom:manifestFile"

# Remove re2j optional source file (re2j uses Bazel, not packaged for openEuler)
rm src/main/java/org/jsoup/helper/Re2jRegex.java
# Remove dead Re2jRegex reference in Regex.java (re2j not on classpath, branch never taken)
sed -i '/Re2jRegex\.compile/d' src/main/java/org/jsoup/helper/Regex.java


%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md CHANGES.md

%files javadoc -f .mfiles-javadoc
%license LICENSE
%exclude %{_javadocdir}/%{name}/src-html

%changelog
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 1.22.2-1
- Initial package for jsoup 1.22.2
