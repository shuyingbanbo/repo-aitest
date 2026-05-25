%{?nodejs_find_provides_and_requires}
%global packagename decamelize

Name:           nodejs-decamelize
Version:        1.2.0
Release:        1%{?dist}
Summary:        Convert a camelized string into a lowercased one with a custom separator
License:        MIT
URL:            https://github.com/sindresorhus/decamelize
Source0:        decamelize-1.2.0.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging

%description
Convert a camelized string into a lowercased one with a custom separator.

%prep
%autosetup -n decamelize-1.2.0

%build
# nothing to do!

%install
if [ -f license ]; then
    mv license LICENSE
fi
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -ra * %{buildroot}%{nodejs_sitelib}/%{packagename}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

%files
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 1.2.0-1
- Initial package
