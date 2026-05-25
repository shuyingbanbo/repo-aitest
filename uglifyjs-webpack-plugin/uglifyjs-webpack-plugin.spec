%global __nodejs_requires %{nil}
%{?nodejs_find_provides_and_requires}
%global packagename uglifyjs-webpack-plugin

Name:           nodejs-uglifyjs-webpack-plugin
Version:        1.0.0~beta.0
Release:        1%{?dist}
Summary:        UglifyJS plugin for webpack
License:        MIT
URL:            https://github.com/webpack-contrib/uglifyjs-webpack-plugin
Source0:        uglifyjs-webpack-plugin-1.0.0-beta.0.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging
Requires:       nodejs-source-map
Requires:       nodejs-uglify-js
Requires:       nodejs-webpack-sources

%description
UglifyJS plugin for webpack.

%prep
%autosetup -n uglifyjs-webpack-plugin-1.0.0-beta.0

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
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 1.0.0~beta.0-1
- Initial package
