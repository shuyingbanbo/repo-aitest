# compat package: official has python3-urllib3-1.26.18
# force_compat mode: introducing 2.7.0 alongside official as python3-urllib3-2
# Fix: urllib3 uses hatch-vcs for dynamic version. We patch pyproject.toml using Python.
Name:           python-urllib3-2
Version:        2.7.0
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling (compat 2.x)
License:        MIT
URL:            https://urllib3.readthedocs.io/
Source0:        %{pypi_source urllib3}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling >= 1.27.0

%description
urllib3 is a powerful, user-friendly HTTP client for Python.
This is the compat package providing version 2.x alongside the system
python3-urllib3 package.


%package -n python3-urllib3-2
Summary:        HTTP library with thread-safe connection pooling (compat 2.x)
Provides:       python3dist(urllib3) = %{version}
Provides:       python-urllib3-2

%description -n python3-urllib3-2
urllib3 is a powerful, user-friendly HTTP client for Python.
This is the compat package providing version 2.x alongside the system
python3-urllib3 package.


%package help
Summary:        Development documents for urllib3-2
Requires:       python3-urllib3-2 = %{version}-%{release}

%description help
Documentation for urllib3 2.x.


%prep
%autosetup -n urllib3-%{version} -p1
# Patch pyproject.toml: remove hatch-vcs/setuptools-scm deps and switch version source
python3 - << 'PYPATCH'
import re

with open('pyproject.toml') as f:
    content = f.read()

# Remove hatch-vcs and setuptools-scm from build-system requires
content = content.replace(', "hatch-vcs>=0.4.0,<0.6.0"', '')
content = content.replace(', "setuptools-scm>=8,<11"', '')

# Replace [tool.hatch.version] section to use static file source
content = re.sub(
    r'\[tool\.hatch\.version\]\nsource = "vcs"\n',
    '[tool.hatch.version]\nsource = "regex"\npath = "src/urllib3/_version.py"\npattern = \'__version__ = "(?P<version>[^"]+)"\'\n',
    content
)

# Remove raw-options and build.hooks.vcs sections
content = re.sub(r'\[tool\.hatch\.version\.raw-options\].*?(?=\[)', '', content, flags=re.DOTALL)
content = re.sub(r'\[tool\.hatch\.build\.hooks\.vcs\].*?(?=\[)', '', content, flags=re.DOTALL)

with open('pyproject.toml', 'w') as f:
    f.write(content)
print('pyproject.toml patched successfully')
PYPATCH

# Create static _version.py
mkdir -p src/urllib3
echo '__version__ = "2.7.0"' > src/urllib3/_version.py

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-urllib3-2
%license LICENSE.txt
%{python3_sitelib}/urllib3/
%{python3_sitelib}/urllib3-%{version}*.dist-info/

%files help
%license LICENSE.txt
%doc README.md CHANGES.rst

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 2.7.0-1
- Initial compat package alongside system python3-urllib3-1.26.18
- Patch pyproject.toml to use static regex version source instead of vcs
