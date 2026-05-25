%global packagename cliui
%global __nodejs_requires %{nil}

Name:           nodejs-cliui
Version:        2.1.0
Release:        1%{?dist}
Summary:        Easily create complex multi-column command-line-interfaces
License:        ISC
URL:            https://github.com/yargs/cliui
Source0:        cliui-2.1.0.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging
Requires:       nodejs-center-align
Requires:       nodejs-right-align
Requires:       nodejs-wordwrap

%description
cliui allows you to easily create complex multi-column command-line-interfaces.

%prep
%autosetup -n cliui-2.1.0

%build
# nothing to do - pure JavaScript

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -a index.js package.json %{buildroot}%{nodejs_sitelib}/%{packagename}/
cp LICENSE.txt %{buildroot}%{nodejs_sitelib}/%{packagename}/LICENSE
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%license %{nodejs_sitelib}/%{packagename}/LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Mon May 25 2026 OpenEuler AI <ai@openeuler.org> - 2.1.0-1
- Initial package for cliui 2.1.0
