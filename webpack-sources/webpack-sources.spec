%global __nodejs_requires %{nil}
%{?nodejs_find_provides_and_requires}
%global packagename webpack-sources

Name:           nodejs-webpack-sources
Version:        1.0.1
Release:        1%{?dist}
Summary:        Source code handling classes for webpack
License:        MIT
URL:            https://github.com/webpack/webpack-sources
Source0:        webpack-sources-1.0.1.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging
Requires:       nodejs-source-list-map
Requires:       nodejs-source-map

%description
Source code handling classes for webpack.

%prep
%autosetup -n webpack-sources-1.0.1

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -ra * %{buildroot}%{nodejs_sitelib}/%{packagename}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%{nodejs_sitelib}/%{packagename}

%changelog
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 1.0.1-1
- Initial package
