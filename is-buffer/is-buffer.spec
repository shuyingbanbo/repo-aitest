%{?nodejs_find_provides_and_requires}
%global packagename is-buffer

Name:           nodejs-is-buffer
Version:        1.1.6
Release:        1%{?dist}
Summary:        Determine if an object is a Buffer
License:        MIT
URL:            https://github.com/feross/is-buffer
Source0:        nodejs-is-buffer-1.1.6.tar.gz

ExclusiveArch:  %{nodejs_arches} noarch
BuildArch:      noarch

BuildRequires:  nodejs-packaging

%description
Determine if an object is a Buffer (safe to use without the
Buffer global being defined).

%prep
%autosetup -n nodejs-is-buffer-1.1.6

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
* Mon May 25 2026 OpenEuler Buildsystem <obs@openeuler.org> - 1.1.6-1
- Initial package
