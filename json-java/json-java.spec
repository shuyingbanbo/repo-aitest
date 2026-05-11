Name:           json-java
Version:        20250517
Release:        1%{?dist}
Summary:        JSON encoder/decoder library for Java

License:        LicenseRef-PublicDomain
URL:            https://github.com/stleary/JSON-java
Source0:        json-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local

%description
JSON in Java is a reference implementation of a JSON encoder/decoder in Java.
It also includes the capability to convert between JSON and XML, HTTP headers,
Cookies, and CDL. The library provides classes such as JSONObject, JSONArray,
JSONTokener, and XMLTokenizer.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
Group:          Documentation
Packager:       openEuler Builder <builder@openeuler.org>

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n json-%{version}

# Change packaging from bundle to jar (maven-bundle-plugin not available)
%pom_xpath_set "pom:project/pom:packaging" "jar"

# Remove bundle plugin (requires bundle packaging)
%pom_remove_plugin -r org.apache.felix:maven-bundle-plugin

# Remove publish/sign plugins not needed in openEuler build environment
%pom_remove_plugin -r :nexus-staging-maven-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-source-plugin

# Remove moditect plugin (module-info generation, not needed for JDK8 target)
%pom_remove_plugin -r org.moditect:moditect-maven-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 20250517-1
- Initial package for json-java 20250517
