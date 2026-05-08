%global debug_package %{nil}

Name:           ripgrep
Version:        15.1.0
Release:        1%{?dist}
Summary:        A line-oriented search tool that recursively searches for a regex pattern

License:        MIT OR Unlicense
URL:            https://github.com/BurntSushi/ripgrep
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rust >= 1.85
BuildRequires:  cargo

%description
ripgrep is a line-oriented search tool that recursively searches the current
directory for a regex pattern. By default, ripgrep will respect gitignore rules
and automatically skip hidden files/directories and binary files. ripgrep has
first class support on Windows, macOS and Linux.

%prep
%setup -q

%build
export CARGO_HOME=$(pwd)/.cargo-home
mkdir -p ${CARGO_HOME}
export CARGO_NET_OFFLINE=true

cargo build --release --offline 2>&1

%install
install -D -m 755 target/release/rg %{buildroot}%{_bindir}/rg

# Shell completions (generated during build if available)
if [ -d target/release/build ]; then
  BASH_COMP=$(find target/release/build -name "rg.bash" 2>/dev/null | head -1)
  FISH_COMP=$(find target/release/build -name "rg.fish" 2>/dev/null | head -1)
  ZSH_COMP=$(find target/release/build -name "_rg" 2>/dev/null | head -1)
  [ -n "${BASH_COMP}" ] && install -D -m 644 "${BASH_COMP}" %{buildroot}%{_datadir}/bash-completion/completions/rg || true
  [ -n "${FISH_COMP}" ] && install -D -m 644 "${FISH_COMP}" %{buildroot}%{_datadir}/fish/vendor_completions.d/rg.fish || true
  [ -n "${ZSH_COMP}" ] && install -D -m 644 "${ZSH_COMP}" %{buildroot}%{_datadir}/zsh/site-functions/_rg || true
fi

# Man page
if [ -d target/release/build ]; then
  MAN_FILE=$(find target/release/build -name "rg.1" 2>/dev/null | head -1)
  [ -n "${MAN_FILE}" ] && install -D -m 644 "${MAN_FILE}" %{buildroot}%{_mandir}/man1/rg.1 || true
fi

%files
%license LICENSE-MIT UNLICENSE COPYING
%doc README.md CHANGELOG.md GUIDE.md FAQ.md
%{_bindir}/rg

%changelog
* Fri May 08 2026 OpenEuler AI Bot <ai@openeuler.org> - 15.1.0-1
- Initial package for ripgrep 15.1.0
