Name:           commons-email
Version:        1.6.0
Release:        1%{?dist}
Summary:        Apache Commons library for sending email via JavaMail API

License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-email
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.mail:jakarta.mail)

%description
Apache Commons Email provides an API for sending email, simplifying the
JavaMail API. It supports plain text, HTML, and multipart emails, as well
as attachments and inline images.

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
# Inject groupId inherited from commons-parent
%pom_xpath_inject "pom:project" "<groupId>org.apache.commons</groupId>"

# Remove plugins not available or not needed in openEuler build environment
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-scm-publish-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r org.apache.commons:commons-release-plugin
%pom_remove_plugin -r com.github.spotbugs:spotbugs-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-assembly-plugin
%pom_remove_plugin -r :maven-pmd-plugin
%pom_remove_plugin -r :maven-changes-plugin

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
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 1.6.0-1
- Initial package for commons-email 1.6.0
