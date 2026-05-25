%global __nodejs_requires %{nil}
%{?nodejs_find_provides_and_requires}
%global packagename uglify-js

Name:           nodejs-uglify-js
Version:        2.8.29
Release:        1%{?dist}
Summary:        JavaScript parser, mangler/compressor and beautifier toolkit
License:        BSD-2-Clause
URL:            https://github.com/mishoo/UglifyJS
Source0:        uglify-js-2.8.29.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging
Requires:       nodejs-source-map
Requires:       nodejs-yargs

%description
UglifyJS is a JavaScript parser, minifier, compressor and beautifier toolkit.

%prep
%autosetup -n uglify-js-2.8.29

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{_bindir}
cp -a bin/uglifyjs %{buildroot}%{_bindir}/uglifyjs

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -ra * %{buildroot}%{nodejs_sitelib}/%{packagename}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%license LICENSE
%{_bindir}/uglifyjs
%{nodejs_sitelib}/%{packagename}

%changelog
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 2.8.29-1
- Initial compat package (official has 2.8.22)
