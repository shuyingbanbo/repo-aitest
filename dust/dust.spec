%global debug_package %{nil}

Name:           dust
Version:        1.2.4
Release:        1%{?dist}
Summary:        A more intuitive version of du
Group:          Applications/System
Packager:       OpenEuler Packaging Team <packaging@openeuler.org>

License:        Apache-2.0
URL:            https://github.com/bootandy/dust
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo

%description
Dust is meant to give you an instant overview of which directories using
disk space without requiring sort or head. Dust will print a maximum of one
'Did not have permissions message'.

Dust lists the biggest folders and files and will intelligently traverse
the tree to find the larger ones. There is no need for a '-d' flag or a
'-h' flag. The largest entries will be colored.

%prep
%autosetup -n %{name}-%{version}

%build
export CARGO_HOME="%{_builddir}/.cargo-home"
export RUSTFLAGS="-C force-frame-pointers=yes"
cargo build --release --offline

%install
install -D -m 755 target/release/dust %{buildroot}%{_bindir}/dust

# Man page
install -D -m 644 man-page/dust.1 %{buildroot}%{_mandir}/man1/dust.1

# Bash completion
install -D -m 644 completions/dust.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/dust

# Zsh completion
install -D -m 644 completions/_dust \
    %{buildroot}%{_datadir}/zsh/site-functions/_dust

# Fish completion
install -D -m 644 completions/dust.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/dust.fish

%files
%license LICENSE
%doc README.md
%{_bindir}/dust
%{_mandir}/man1/dust.1*
%{_datadir}/bash-completion/completions/dust
%{_datadir}/zsh/site-functions/_dust
%{_datadir}/fish/vendor_completions.d/dust.fish

%changelog
* Wed May 20 2026 OpenEuler Packaging Team <packaging@openeuler.org> - 1.2.4-1
- Initial RPM package for dust 1.2.4
