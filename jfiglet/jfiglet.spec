Name:           jfiglet
Version:        0.0.8
Release:        1%{?dist}
Summary:        Java implementation of FIGfonts to create ASCII art banners
BuildArch:      noarch
License:        GPL-2.0-only
URL:            https://github.com/lalyos/jfiglet
Source0:        jfiglet-0.0.8.tar.gz
Group:          Development/Libraries/Java
Packager:       Java_Bot <Java_Bot@openeuler.org>

BuildRequires:  maven-local

%description
jfiglet is a Java implementation of FIGfonts (http://www.figlet.org/)
to create ASCII art banners. It can be used as a Maven dependency or
from the command line.

%package help
Summary:        API documentation for %{name}
%description help
Documentation for %{name}.

%prep
%autosetup -n jfiglet-0.0.8
# Remove plugins not needed for offline build
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :nexus-staging-maven-plugin
# Remove sonatype parent pom dependency (requires network)
%pom_remove_parent

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%files help -f .mfiles-javadoc
%license LICENSE

%changelog
* Sat May 09 2026 Java_Bot <Java_Bot@openeuler.org> - 0.0.8-1
- Initial package
