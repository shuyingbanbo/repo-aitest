%{?nodejs_find_provides_and_requires}
%global packagename lazy-cache
Name:           nodejs-lazy-cache
Version:        1.0.4
Release:        1%{?dist}
Summary:        Cache requires to be lazy-loaded when needed
License:        MIT
URL:            https://github.com/jonschlinkert/lazy-cache
Source0:        lazy-cache-1.0.4.tar.gz
ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs
%description
Cache requires to be lazy-loaded only when they are needed.
%prep
%autosetup -n lazy-cache-1.0.4
%build
%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -a index.js package.json LICENSE %{buildroot}%{nodejs_sitelib}/%{packagename}/
%nodejs_symlink_deps
%check
%nodejs_symlink_deps --check
%files
%license %{nodejs_sitelib}/%{packagename}/LICENSE
%{nodejs_sitelib}/%{packagename}
%changelog
* Mon May 25 2026 OpenEuler AI <ai@openeuler.org> - 1.0.4-1
- Initial package
