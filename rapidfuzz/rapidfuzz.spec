Name:           python-rapidfuzz
Version:        3.9.7
Release:        1%{?dist}
Summary:        Rapid fuzzy string matching in Python using various string metrics
License:        MIT
URL:            https://github.com/maxbachmann/RapidFuzz
BuildArch:      aarch64

# Pre-built from manylinux wheel; source build requires Cython >=3.0.11 not yet in OpenEuler
Source0:        https://files.pythonhosted.org/packages/06/09/efe65f1b01e1778e57b8f29e9f8d39c8203c6022698a246f6c57e8471000/rapidfuzz-3.9.7-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl

BuildRequires:  python3-devel
BuildRequires:  python3-pip

%description
RapidFuzz is a fast string matching library for Python and C++.


%package -n python3-rapidfuzz
Summary:        Rapid fuzzy string matching in Python
Provides:       python-rapidfuzz
Provides:       python3dist(rapidfuzz) = %{version}

%description -n python3-rapidfuzz
RapidFuzz is a fast string matching library for Python and C++.


%prep
# Install from pre-built wheel (Cython dependency not available)
cp %{SOURCE0} /tmp/rapidfuzz-3.9.7-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl

%build
echo "Using pre-built wheel"

%install
pip3 install --root %{buildroot} --no-compile --no-index /tmp/rapidfuzz-3.9.7-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl

%files -n python3-rapidfuzz
/usr/lib64/python3.11/site-packages/rapidfuzz/
/usr/lib64/python3.11/site-packages/rapidfuzz-%{version}*.dist-info/

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 3.9.7-1
- Package from manylinux aarch64 wheel (Cython not available for source build)
