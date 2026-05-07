%global debug_package %{nil}

Name:           fzf
Version:        0.72
Release:        1%{?dist}
Summary:        A command-line fuzzy finder

License:        MIT
URL:            https://github.com/junegunn/fzf
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang >= 1.23
BuildRequires:  make

%description
fzf is a general-purpose command-line fuzzy finder.
It is an interactive filter program for any kind of list; files, command
history, processes, hostnames, bookmarks, git commits, etc.

%prep
%setup -q

%build
export CGO_ENABLED=0
export GOPROXY=off
export GOFLAGS=-buildvcs=false
export FZF_VERSION=0.72
export FZF_REVISION=tarball

go build -mod=vendor \
    -ldflags "-s -w -X main.version=${FZF_VERSION} -X main.revision=${FZF_REVISION}" \
    -o fzf .

%install
# Binary
install -D -m 755 fzf %{buildroot}%{_bindir}/fzf

# fzf-tmux helper script
install -D -m 755 bin/fzf-tmux %{buildroot}%{_bindir}/fzf-tmux

# Shell completion & key bindings
install -D -m 644 shell/completion.bash %{buildroot}%{_datadir}/fzf/completion.bash
install -D -m 644 shell/completion.zsh  %{buildroot}%{_datadir}/fzf/completion.zsh
install -D -m 644 shell/completion.fish %{buildroot}%{_datadir}/fzf/completion.fish
install -D -m 644 shell/key-bindings.bash %{buildroot}%{_datadir}/fzf/key-bindings.bash
install -D -m 644 shell/key-bindings.zsh  %{buildroot}%{_datadir}/fzf/key-bindings.zsh
install -D -m 644 shell/key-bindings.fish %{buildroot}%{_datadir}/fzf/key-bindings.fish

# Man pages
install -D -m 644 man/man1/fzf.1      %{buildroot}%{_mandir}/man1/fzf.1
install -D -m 644 man/man1/fzf-tmux.1 %{buildroot}%{_mandir}/man1/fzf-tmux.1

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/fzf
%{_bindir}/fzf-tmux
%{_datadir}/fzf/
%{_mandir}/man1/fzf.1*
%{_mandir}/man1/fzf-tmux.1*

%changelog
* Thu May 07 2026 OpenEuler AI Bot <ai@openeuler.org> - 0.72-1
- Initial package for fzf 0.72
