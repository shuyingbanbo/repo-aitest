%global __nodejs_requires %{nil}
%{?nodejs_find_provides_and_requires}
%global packagename align-text

Name:           nodejs-align-text
Version:        0.1.4
Release:        1%{?dist}
Summary:        Align the text in a string
License:        MIT
URL:            https://github.com/jonschlinkert/align-text
Source0:        align-text-0.1.4.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging
Requires:       nodejs-kind-of
Requires:       nodejs-longest
Requires:       nodejs-repeat-string

%description
Align the text in a string.

%prep
%autosetup -n align-text-0.1.4

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
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 0.1.4-1
- Initial package
