Name:           jspecify
Version:        1.0.0
Release:        1%{?dist}
Summary:        Standard annotations for Java null safety static analysis

License:        Apache-2.0
URL:            https://jspecify.dev
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local

%description
JSpecify provides standard annotations for static analysis tools to check
Java code for null safety. Annotations include @Nullable, @NonNull,
@NullMarked, and @NullUnmarked.

This package provides a compatible implementation of the jspecify 1.0.0
annotation API for use as a build-time dependency.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
Group:          Documentation
Packager:       openEuler Builder <builder@openeuler.org>

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 1.0.0-1
- Stub package providing jspecify annotation API for build-time use
