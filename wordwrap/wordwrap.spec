%{?nodejs_find_provides_and_requires}
%global packagename wordwrap
Name:           nodejs-wordwrap
Version:        0.0.2
Release:        1%{?dist}
Summary:        Wrap those words. Show them at what columns to start and stop
License:        MIT
URL:            https://github.com/substack/node-wordwrap
Source0:        wordwrap-0.0.2.tar.gz
ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs
%description
Wrap words. Show them at what columns to start and stop.
%prep
%autosetup -n wordwrap-0.0.2
%build
%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -a index.js package.json %{buildroot}%{nodejs_sitelib}/%{packagename}/
[ -f LICENSE ] && cp LICENSE %{buildroot}%{nodejs_sitelib}/%{packagename}/ || true
%nodejs_symlink_deps
%check
%nodejs_symlink_deps --check
%files
%{nodejs_sitelib}/%{packagename}
%changelog
* Mon May 25 2026 OpenEuler AI <ai@openeuler.org> - 0.0.2-1
- Initial package
