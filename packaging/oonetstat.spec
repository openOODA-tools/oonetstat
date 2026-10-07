Name:           oonetstat
Version:        0.1.0
Release:        1%{?dist}
Summary:        Inspects open TCP, UDP, and UNIX domain sockets, routing tables, and interface stats.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oonetstat
Source0:        oonetstat-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oonetstat is a sovereign, capability-bounded SOCKET AUDITOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oonetstat
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oonetstat-uninstall

%files
/usr/bin/oonetstat
/usr/bin/oonetstat-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
