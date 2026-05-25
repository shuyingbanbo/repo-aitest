%global __nodejs_requires %{nil}
%{?nodejs_find_provides_and_requires}
%global packagename yargs

Name:           nodejs-yargs
Version:        3.10.0
Release:        1%{?dist}
Summary:        Light-weight option parsing with an argv hash
License:        MIT
URL:            https://github.com/yargs/yargs
Source0:        yargs-3.10.0.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging
Requires:       nodejs-camelcase
Requires:       nodejs-cliui
Requires:       nodejs-decamelize
Requires:       nodejs-window-size

%description
Light-weight option parsing with an argv hash. No optstrings attached.

%prep
%autosetup -n yargs-3.10.0

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
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 3.10.0-1
- Initial package
