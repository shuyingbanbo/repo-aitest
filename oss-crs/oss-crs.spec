Name:           python-oss-crs
Version:        0.1.0
Release:        1%{?dist}
Summary:        Cyber Reasoning System orchestration framework for bug finding and fixing
License:        MIT
URL:            https://github.com/ossf/oss-crs
Source0:        %{pypi_source oss-crs}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-setuptools >= 61.0
BuildRequires:  python3-wheel

%description
OSS-CRS is a standard orchestration framework for building and running
LLM-based autonomous bug-finding and bug-fixing systems (Cyber Reasoning
Systems). It defines a unified interface for CRS development and supports
running CRSs against OSS-Fuzz compatible projects.


%package -n python3-oss-crs
Summary:        Cyber Reasoning System orchestration framework for bug finding and fixing
Provides:       python-oss-crs
Provides:       python3dist(oss-crs) = %{version}
Requires:       python3-requests >= 2.31.0
Requires:       python3-pyyaml >= 6.0.1
Requires:       python3-jinja2 >= 3.1.3
Requires:       python3-dotenv >= 1.0.1
Requires:       python3-docker >= 7.0.0
Requires:       python3-ruff >= 0.7.0
Requires:       python3-pyright >= 1.1.407
Requires:       python3-GitPython >= 3.1.45
Requires:       python3-pydantic >= 2.10.6
Requires:       python3-rich >= 13.7.0
Requires:       python3-questionary >= 2.1.1

%description -n python3-oss-crs
OSS-CRS is a standard orchestration framework for building and running
LLM-based autonomous bug-finding and bug-fixing systems (Cyber Reasoning
Systems). It defines a unified interface for CRS development and supports
running CRSs against OSS-Fuzz compatible projects.


%package help
Summary:        Development documents and examples for python-oss-crs
Provides:       python3-oss-crs-doc
Requires:       python3-oss-crs

%description help
Development documents and examples for python-oss-crs.


%prep
%autosetup -n oss-crs-%{version} -p1
# setuptools 68 requires license as table, not plain string
sed -i 's/^license = "MIT"$/license = {text = "MIT"}/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install
# Strip Requires-Dist entries whose version constraints exceed what OpenEuler provides,
# so pythondistdeps.py does not generate unresolvable auto-Requires.
find %{buildroot}%{python3_sitelib} -name 'METADATA' -path '*/oss_crs*' | \
  xargs -r sed -i \
    -e '/^Requires-Dist: PyYAML/d' \
    -e '/^Requires-Dist: Jinja2/d' \
    -e '/^Requires-Dist: docker/d' \
    -e '/^Requires-Dist: ruff/d' \
    -e '/^Requires-Dist: pydantic/d'

%check
# Tests require network access and Docker daemon; skip in offline build environment

%files -n python3-oss-crs
%license LICENSE
%{python3_sitelib}/oss_crs/
%{python3_sitelib}/oss_crs-%{version}*.dist-info/
%{_bindir}/oss-crs

%files help
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
* Thu May 28 2026 Python_Bot <Python_Bot@openeuler.org> - 0.1.0-1
- Initial package
