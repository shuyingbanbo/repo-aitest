%global __nodejs_requires %{nil}
%{?nodejs_find_provides_and_requires}
%global packagename right-align
Name:           nodejs-right-align
Version:        0.1.3
Release:        1%{?dist}
Summary:        Right-align the text in a string
License:        MIT
URL:            https://github.com/jonschlinkert/right-align
Source0:        right-align-0.1.3.tar.gz
ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs
%description
Right-align the text in a string.
%prep
%autosetup -n right-align-0.1.3
%build
%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -a index.js package.json %{buildroot}%{nodejs_sitelib}/%{packagename}/
[ -f LICENSE ] && cp LICENSE %{buildroot}%{nodejs_sitelib}/%{packagename}/ || true
[ -f LICENSE.md ] && cp LICENSE.md %{buildroot}%{nodejs_sitelib}/%{packagename}/LICENSE || true
%nodejs_symlink_deps
%check
%nodejs_symlink_deps --check
%files
%{nodejs_sitelib}/%{packagename}
%changelog
* Mon May 25 2026 OpenEuler AI <ai@openeuler.org> - 0.1.3-1
- Initial package
