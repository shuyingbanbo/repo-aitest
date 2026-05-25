%{?nodejs_find_provides_and_requires}
%global packagename longest

Name:           nodejs-longest
Version:        1.0.1
Release:        1%{?dist}
Summary:        Get the longest item in an array
License:        MIT
URL:            https://github.com/jonschlinkert/longest
Source0:        longest-1.0.1.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging

%description
Get the longest item in an array.

%prep
%autosetup -n longest-1.0.1

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
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 1.0.1-1
- Initial package
