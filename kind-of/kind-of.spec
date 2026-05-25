%global __nodejs_requires %{nil}
%{?nodejs_find_provides_and_requires}
%global packagename kind-of

Name:           nodejs-kind-of
Version:        3.2.2
Release:        1%{?dist}
Summary:        Get the native type of a value
License:        MIT
URL:            https://github.com/jonschlinkert/kind-of
Source0:        kind-of-3.2.2.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging
Requires:       nodejs-is-buffer

%description
Get the native type of a value.

%prep
%autosetup -n kind-of-3.2.2

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
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 3.2.2-1
- Initial package
