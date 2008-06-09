%define libfontenc %mklibname fontenc 1
Name: libfontenc
Summary:  The fontenc Library
Version: 1.0.4
Release: %mkrel 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libfontenc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: zlib-devel
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
# list of encodings
Requires: x11-font-encodings

%description
libfontenc is a library which helps font libraries portably determine and 
deal with different encodings of fonts.

#-----------------------------------------------------------

%package -n %{libfontenc}
Summary:  The fontenc Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libfontenc}
libfontenc is a library which helps font libraries portably determine and 
deal with different encodings of fonts.

#-----------------------------------------------------------

%package -n %{libfontenc}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libfontenc} = %{version}
Provides: libfontenc-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{libfontenc}-devel
Development files for %{name}

%pre -n %{libfontenc}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libfontenc}-devel
%defattr(-,root,root)
%{_libdir}/libfontenc.so
%{_libdir}/libfontenc.la
%{_libdir}/pkgconfig/fontenc.pc
%{_includedir}/X11/fonts/fontenc.h

#-----------------------------------------------------------

%package -n %{libfontenc}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libfontenc}-devel = %{version}
Provides: libfontenc-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libfontenc}-static-devel
Static development files for %{name}

%files -n %{libfontenc}-static-devel
%defattr(-,root,root)
%{_libdir}/libfontenc.a

#-----------------------------------------------------------

%prep
%setup -q -n libfontenc-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}\
		--with-encodingsdir=%{_datadir}/fonts/encodings

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libfontenc}
%defattr(-,root,root)
%{_libdir}/libfontenc.so.1
%{_libdir}/libfontenc.so.1.0.0


