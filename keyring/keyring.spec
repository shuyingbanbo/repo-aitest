# compat package: official has python3-keyring-23.13.1
# force_compat: introducing 25.7.0 as python3-keyring-25
Name:           python-keyring-25
Version:        25.7.0
Release:        1%{?dist}
Summary:        Store and access your passwords safely (compat 25)
License:        MIT
URL:            https://github.com/jaraco/keyring
Source0:        %{pypi_source keyring}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm >= 3.4.1
BuildRequires:  pyproject-rpm-macros

%description
A utility to store and retrieve passwords using various platform backends.
This is the compat package providing version 25.x alongside the system keyring.


%package -n python3-keyring-25
Summary:        Store and access your passwords safely (compat 25)
Requires:       python3-SecretStorage >= 3.2
Requires:       python3-jeepney >= 0.4.2
Requires:       python3-importlib-metadata >= 4.11.4
Requires:       python3-jaraco-classes
Requires:       python3-jaraco-functools
Requires:       python3-jaraco-context
Provides:       python3dist(keyring) = %{version}
Provides:       python-keyring-25

%description -n python3-keyring-25
A utility to store and retrieve passwords using various platform backends.
This is the compat package providing version 25.x alongside the system keyring.


%package help
Summary:        Documentation for keyring-25
Requires:       python3-keyring-25 = %{version}-%{release}

%description help
Documentation for keyring 25.x.


%prep
%autosetup -n keyring-%{version} -p1
# Remove coherent.licensed (license header tool) and fix setuptools version constraint
python3 - << 'PYPATCH'
import re
with open('pyproject.toml') as f:
    content = f.read()
# Remove coherent.licensed from build-system requires
# Remove coherent.licensed line and its preceding comment
lines = content.split('\n')
new_lines = []
skip_next = False
for i, line in enumerate(lines):
    if '"coherent.licensed"' in line:
        # Also remove the comment line before it (if any)
        if new_lines and new_lines[-1].strip().startswith('#'):
            new_lines.pop()
        skip_next = False
        continue
    new_lines.append(line)
content = '\n'.join(new_lines)
# Relax setuptools requirement for older setuptools
content = re.sub(r'"setuptools>=\d+",', '"setuptools",', content)
# Create static _version.py (setuptools_scm not available above 8)
# Also fix license format for older setuptools
content = content.replace('license = \"MIT\"', 'license = {text = \"MIT\"}')
with open('pyproject.toml', 'w') as f:
    f.write(content)
print('pyproject.toml patched')
PYPATCH
# Create static version file for setuptools_scm
echo '__version__ = "25.7.0"' > keyring/_version.py

%build
%pyproject_build

%install
%pyproject_install
# Create LICENSE file since keyring uses inline license in pyproject.toml
mkdir -p %{buildroot}%{_datadir}/licenses/python3-keyring-25
echo "MIT License" > %{buildroot}%{_datadir}/licenses/python3-keyring-25/LICENSE
# Remove pywin32-ctypes from METADATA Requires-Dist if present
find %{buildroot}%{python3_sitelib} -name "METADATA" -path "*/keyring*" | xargs -r grep -l "pywin32" | xargs -r sed -i '/Requires-Dist: pywin32/d'

%files -n python3-keyring-25
%{_datadir}/licenses/python3-keyring-25/
%{python3_sitelib}/keyring/
%{python3_sitelib}/keyring-*.dist-info/
%{_bindir}/keyring

%files help
%doc README.rst
%doc README.rst

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 25.7.0-1
- Initial compat package alongside system python3-keyring-23.13.1
