%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib/rpm/brp-python-bytecompile[^ ]* [^ ]* [^ ]* [^ ]*!!g')

Name:           python-ngs-mapper
Version:        1.5.0
Release:        1%{?dist}
Summary:        Pipeline that combines sff and fastq from multiple platforms
License:        GPL-2.0-only
URL:            https://github.com/VDBWRAIR/ngs_mapper
Source0:        %{url}/archive/v%{version}/ngs_mapper-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
ngs_mapper is a pipeline that combines sff and fastq reads from multiple
sequencing platforms (Roche 454, Ion Torrent, Illumina MiSeq) and maps
them to a reference sequence, producing consensus sequences and variant
calls.


%package -n python3-ngs-mapper
Summary:        Pipeline that combines sff and fastq from multiple platforms
Provides:       python-ngs-mapper
Provides:       python3dist(ngs-mapper) = %{version}

%description -n python3-ngs-mapper
ngs_mapper is a pipeline that combines sff and fastq reads from multiple
sequencing platforms (Roche 454, Ion Torrent, Illumina MiSeq) and maps
them to a reference sequence, producing consensus sequences and variant
calls.


%package help
Summary:        Development documents and examples for python-ngs-mapper
Provides:       python3-ngs-mapper-doc

%description help
Documentation and examples for python-ngs-mapper.


%prep
%autosetup -n ngs_mapper-%{version} -p1

%build
%py3_build

%install
# ngs_mapper 1.5.0 is a Python 2 codebase; disable byte-compilation to avoid
# SyntaxError on Python 2 print statements and except X, e: syntax
/usr/bin/python3 setup.py install --no-compile --skip-build \
  --root %{buildroot}

%files -n python3-ngs-mapper
%license LICENSE
%{python3_sitelib}/ngs_mapper/
%{python3_sitelib}/ngs_mapper-%{version}*.egg-info/
%{_bindir}/is_sanger
%{_bindir}/convert_sangers
%{_bindir}/sff_to_fastq
%{_bindir}/convert_formats
%{_bindir}/ngs_filter
%{_bindir}/roche_sync
%{_bindir}/sample_coverage
%{_bindir}/make_example_config
%{_bindir}/base_caller
%{_bindir}/ion_sync
%{_bindir}/fqstats
%{_bindir}/graph_mapunmap
%{_bindir}/graphsample
%{_bindir}/graph_times
%{_bindir}/miseq_sync
%{_bindir}/rename_sample
%{_bindir}/run_bwa_on_samplename
%{_bindir}/runsample
%{_bindir}/sanger_sync
%{_bindir}/stats_at_refpos
%{_bindir}/tagreads
%{_bindir}/trim_reads
%{_bindir}/vcf_consensus
%{_bindir}/vcf_diff
%{_bindir}/lf_consensus
%{_bindir}/consensuses.sh
%{_bindir}/gen_flagstats.sh
%{_bindir}/graphs.sh
%{_bindir}/pilon.sh
%{_bindir}/runsamplesheet.sh

%files help
%doc README.rst CHANGELOG.rst

%changelog
* Tue May 26 2026 Python_Bot <Python_Bot@openeuler.org> - 1.5.0-1
- Initial package
