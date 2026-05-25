%{?nodejs_find_provides_and_requires}
%global packagename source-list-map

Name:           nodejs-source-list-map
Version:        2.0.1
Release:        1%{?dist}
Summary:        Fast line to line SourceNode implementation for webpack
License:        MIT
URL:            https://github.com/webpack/source-list-map
Source0:        source-list-map-2.0.1.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging

%description
Fast line to line SourceNode implementation for webpack.

%prep
%autosetup -n source-list-map-2.0.1

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
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 2.0.1-1
- Initial package
