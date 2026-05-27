Name:           python-markdown-to-confluence
Version:        0.3.5
Release:        1%{?dist}
Summary:        Publish Markdown files to Confluence wiki
License:        MIT
URL:            https://github.com/hunyadi/md2conf
Source0:        %{pypi_source markdown-to-confluence}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools >= 42
BuildRequires:  python3-wheel
BuildRequires:  python3-lxml
BuildRequires:  python3-markdown
BuildRequires:  python3-pymdown-extensions
BuildRequires:  python3-pyyaml >= 6.0

%description
A tool and Python library to publish Markdown pages to Confluence.


%package -n python3-markdown-to-confluence
Summary:        Publish Markdown files to Confluence wiki
Requires:       python3-lxml
Requires:       python3-markdown
Requires:       python3-pymdown-extensions
Requires:       python3-pyyaml >= 6.0
Requires:       python3-requests >= 2.31.0
Provides:       python-markdown-to-confluence
Provides:       python3dist(markdown-to-confluence) = %{version}

%description -n python3-markdown-to-confluence
A tool and Python library to publish Markdown pages to Confluence.


%package help
Summary:        Documentation for markdown-to-confluence
Requires:       python3-markdown-to-confluence = %{version}-%{release}

%description help
Documentation for markdown-to-confluence.


%prep
%autosetup -n markdown-to-confluence-%{version} -p1
# Relax version constraints since official packages satisfy runtime
sed -i 's/lxml >= 5.4/lxml >= 5.0/' setup.cfg
sed -i 's/markdown >= 3.8/markdown >= 3.6/' setup.cfg
sed -i 's/pymdown-extensions >= 10.15/pymdown-extensions >= 10.0/' setup.cfg
sed -i 's/requests >= 2.32/requests >= 2.31/' setup.cfg
# Remove types-* stub packages from install_requires (not needed at runtime)
sed -i '/types-lxml/d' setup.cfg
sed -i '/types-markdown/d' setup.cfg
sed -i '/types-PyYAML/d' setup.cfg
sed -i '/types-requests/d' setup.cfg

%build
%py3_build

%install
%py3_install

%files -n python3-markdown-to-confluence
%license LICENSE
%{python3_sitelib}/md2conf/
%{python3_sitelib}/markdown_to_confluence-%{version}*.egg-info/
%{_bindir}/md2conf

%files help
%license LICENSE
%doc README.md

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 0.3.5-1
- Initial package
