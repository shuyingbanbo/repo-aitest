Name:           python-mcp-atlassian
Version:        0.13.0
Release:        1%{?dist}
Summary:        MCP server for Atlassian products (Confluence and Jira)
License:        MIT
URL:            https://github.com/sooperset/mcp-atlassian
Source0:        https://github.com/sooperset/mcp-atlassian/archive/v0.13.0/mcp-atlassian-0.13.0.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-uv-dynamic-versioning

%description
Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira).
Supports both Cloud and Server/Data Center deployments. Enables secure, contextual
AI interactions with Atlassian tools while maintaining data privacy and security.


%package -n python3-mcp-atlassian
Summary:        MCP server for Atlassian products (Confluence and Jira)
Provides:       python-mcp-atlassian
Provides:       python3dist(mcp-atlassian) = %{version}
Requires:       python3-atlassian-python-api
Requires:       python3-requests >= 2.31.0
Requires:       python3-beautifulsoup4-4.14
Requires:       python3-httpx-0.28
Requires:       python3-mcp
Requires:       python3-fastmcp
Requires:       python3-dotenv >= 1.0.1
Requires:       python3-markdownify
Requires:       python3-markdown
Requires:       python3-markdown-to-confluence
Requires:       python3-pydantic
Requires:       python3-trio-0.29
Requires:       python3-click
Requires:       python3-uvicorn
Requires:       python3-starlette-1.0
Requires:       python3-urllib3-2
Requires:       python3-thefuzz
Requires:       python3-python-dateutil-2.9
Requires:       python3-types-python-dateutil-2.9
Requires:       python3-keyring-25
Requires:       python3-cachetools
Requires:       python3-types-cachetools
Requires:       python3-truststore
Requires:       python3-fakeredis

%description -n python3-mcp-atlassian
Model Context Protocol (MCP) server for Atlassian products (Confluence and Jira).


%package help
Summary:        Documentation for mcp-atlassian
Requires:       python3-mcp-atlassian = %{version}-%{release}

%description help
Documentation for mcp-atlassian.


%prep
%autosetup -n mcp-atlassian-%{version} -p1
# Create static version file (uv-dynamic-versioning uses git tags)
mkdir -p src/mcp_atlassian
echo '__version__ = "0.13.0"' > src/mcp_atlassian/_version.py
# Patch pyproject.toml: use static version, remove uv-dynamic-versioning
python3 /tmp/patch_mcp_atlassian_pyproject.py

%build
%pyproject_build

%install
%pyproject_install

%check
# Tests require live Atlassian service access (Jira/Confluence/Bitbucket)
# and cannot run in offline build environment.

%files -n python3-mcp-atlassian
%license LICENSE
%{python3_sitelib}/mcp_atlassian/
%{python3_sitelib}/mcp_atlassian-%{version}*.dist-info/
%{_bindir}/mcp-atlassian

%files help
%license LICENSE
%doc README.md

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 0.13.0-1
- Initial package for mcp-atlassian 0.13.0
