%{?nodejs_find_provides_and_requires}
%global packagename camelcase

Name:           nodejs-camelcase
Version:        1.2.1
Release:        1%{?dist}
Summary:        Convert a dash/dot/underscore/space separated string to camelCase
License:        MIT
URL:            https://github.com/sindresorhus/camelcase
Source0:        camelcase-1.2.1.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging
BuildRequires:  nodejs

%description
Convert a dash/dot/underscore/space separated string to camelCase.

%prep
%autosetup -n camelcase-1.2.1

%build
# nothing to do - pure JavaScript

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -a index.js package.json %{buildroot}%{nodejs_sitelib}/%{packagename}/
if [ -f license ]; then cp license %{buildroot}%{nodejs_sitelib}/%{packagename}/LICENSE; fi
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%license %{nodejs_sitelib}/%{packagename}/LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Mon May 25 2026 OpenEuler AI <ai@openeuler.org> - 1.2.1-1
- Initial package for camelcase 1.2.1
