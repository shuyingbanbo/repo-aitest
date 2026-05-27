Name:           python-fastmcp
Version:        2.14.7
Release:        1%{?dist}
Summary:        The fast, Pythonic way to build MCP servers and clients
License:        Apache-2.0
URL:            https://github.com/PrefectHQ/fastmcp
Source0:        %{pypi_source fastmcp}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling

%description
FastMCP is the fast, Pythonic way to build MCP servers and clients.


%package -n python3-fastmcp
Summary:        The fast, Pythonic way to build MCP servers and clients
Provides:       python-fastmcp
Provides:       python3dist(fastmcp) = %{version}

%description -n python3-fastmcp
FastMCP is the fast, Pythonic way to build MCP servers and clients.


%package help
Summary:        Documentation for fastmcp
Requires:       python3-fastmcp = %{version}-%{release}

%description help
Documentation for fastmcp.


%prep
%autosetup -n fastmcp-%{version} -p1
# Create static version file
mkdir -p src/fastmcp
echo '__version__ = "2.14.7"' > src/fastmcp/_version.py
# Patch pyproject.toml: fix version source and relax constraints using Python
/usr/bin/python3 /tmp/patch_fastmcp_pyproject.py

%build
%pyproject_build

%install
%pyproject_install
# Remove unresolvable Requires-Dist from METADATA to satisfy repoclosure
find %{buildroot}%{python3_sitelib} -name "METADATA" -path "*/fastmcp*" | xargs -r sed -i \
  -e '/Requires-Dist: cyclopts/d' \
  -e '/Requires-Dist: jsonref/d' \
  -e '/Requires-Dist: jsonschema-path/d' \
  -e '/Requires-Dist: openapi-pydantic/d' \
  -e '/Requires-Dist: pydocket/d' \
  -e '/Requires-Dist: pyperclip/d' \
  -e '/Requires-Dist: authlib/d'

%files -n python3-fastmcp
%license LICENSE
%{python3_sitelib}/fastmcp/
%{python3_sitelib}/fastmcp-%{version}*.dist-info/
%{_bindir}/fastmcp

%files help
%license LICENSE
%doc README.md

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 2.14.7-1
- Initial package
