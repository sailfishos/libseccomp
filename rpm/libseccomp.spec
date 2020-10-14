Name:           libseccomp
Version:        2.4.2
Release:        1
Summary:        An Enhanced Seccomp (mode 2) Helper Library
License:        LGPLv2
URL:            https://github.com/seccomp/libseccomp.git
Source:         https://github.com/seccomp/libseccomp/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-tests-rely-on-__SNR_xxx-instead-of-__NR_xxx-for-sysc.patch
Patch1:         0002-tests-allow-sb2-to-accelerate-seq-on-SailfishOS.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
The libseccomp library provides and easy to use, platform
independent, interface to the Linux Kernel's syscall filtering
mechanism: seccomp. The libseccomp API is designed to abstract away
the underlying BPF based syscall filter language and present a more
conventional function-call based filtering interface that should be
familiar to, and easily adopted by application developers.

%package devel
Summary:        Development files for libseccomp, an enhanced Seccomp (mode 2) helper library
Requires:       %name = %version

%description devel
The libseccomp library provides and easy to use, platform
independent, interface to the Linux Kernel's syscall filtering
mechanism: seccomp. The libseccomp API is designed to abstract away
the underlying BPF based syscall filter language and present a more
conventional function-call based filtering interface that should be
familiar to, and easily adopted by application developers.

This package contains the development files and debugging utilities
for libseccomp.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%autogen
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}

%make_install
find "%{buildroot}/%{_libdir}" -type f -name "*.la" -delete;
rm -r %{buildroot}/%{_mandir}
%fdupes %{buildroot}/%{_prefix}

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%_libdir/%name.so.2*
%license LICENSE

%files devel
%defattr(-,root,root)
%_includedir/seccomp.h
%_includedir/seccomp-syscalls.h
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_bindir/scmp_sys_resolver
