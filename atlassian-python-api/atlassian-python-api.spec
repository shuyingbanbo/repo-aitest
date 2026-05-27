Name:           python-atlassian-python-api
Version:        4.0.8
Release:        1%{?dist}
Summary:        Python Atlassian REST API Wrapper
License:        Apache-2.0
URL:            https://github.com/atlassian-api/atlassian-python-api
Source0:        %{pypi_source atlassian-python-api}
BuildArch:      noarch

# Build requirements placed in main preamble per openEuler convention
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-deprecated
BuildRequires:  python3-requests
BuildRequires:  python3-oauthlib
BuildRequires:  python3-requests-oauthlib
BuildRequires:  python3-jmespath
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-typing-extensions

%description
Python Atlassian REST API Wrapper for Jira, Confluence, Bitbucket,
Bamboo, Crowd, Portfolio, Tempo, ServiceDesk, and Assets.


%package -n python3-atlassian-python-api
Summary:        Python Atlassian REST API Wrapper
Provides:       python-atlassian-python-api
Provides:       python3dist(atlassian-python-api) = %{version}
Requires:       python3-deprecated
Requires:       python3-requests
Requires:       python3-oauthlib
Requires:       python3-requests-oauthlib
Requires:       python3-jmespath
Requires:       python3-beautifulsoup4
Requires:       python3-typing-extensions

%description -n python3-atlassian-python-api
Python Atlassian REST API Wrapper for Jira, Confluence, Bitbucket,
Bamboo, Crowd, Portfolio, Tempo, ServiceDesk, and Assets.


%package help
Summary:        Development documents and examples for python-atlassian-python-api
Provides:       python3-atlassian-python-api-doc

%description help
Documentation and examples for the atlassian-python-api package.


%prep
%autosetup -n atlassian-python-api-%{version} -p1

%build
%py3_build

%install
%py3_install

# Tests require live Atlassian service access (Jira/Confluence/Bitbucket)
# and cannot run in offline build environment.

%files -n python3-atlassian-python-api
%license LICENSE
%{python3_sitelib}/atlassian/
%{python3_sitelib}/atlassian_python_api-%{version}*.egg-info/

%files help
%doc README.rst

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 4.0.8-1
- Initial package
