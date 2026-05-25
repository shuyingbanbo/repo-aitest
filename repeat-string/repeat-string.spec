%{?nodejs_find_provides_and_requires}
%global packagename repeat-string

Name:           nodejs-repeat-string
Version:        1.6.1
Release:        1%{?dist}
Summary:        Repeat the given string n times
License:        MIT
URL:            https://github.com/jonschlinkert/repeat-string
Source0:        repeat-string-1.6.1.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging

%description
Repeat the given string n times. Fastest implementation for repeating a string.

%prep
%autosetup -n repeat-string-1.6.1

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -ra * %{buildroot}%{nodejs_sitelib}/%{packagename}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 1.6.1-1
- Initial package
