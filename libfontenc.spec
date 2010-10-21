%define major 1
%define libname %mklibname fontenc %{major}
%define develname %mklibname fontenc -d
%define staticdevelname %mklibname fontenc -d -s

Name: libfontenc
Summary:  The fontenc Library
Version: 1.1.0
Release: %mkrel 1
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

%package -n %{libname}
Summary:  The fontenc Library
Group: System/Libraries
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
libfontenc is a library which helps font libraries portably determine and 
deal with different encodings of fonts.

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libfontenc.so.%{major}*

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libfontenc-devel = %{version}-%{release}
Obsoletes: %{_lib}fontenc1-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libfontenc.so
%{_libdir}/libfontenc.la
%{_libdir}/pkgconfig/fontenc.pc
%{_includedir}/X11/fonts/fontenc.h

#-----------------------------------------------------------

%package -n %{staticdevelname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libfontenc-static-devel = %{version}-%{release}
Obsoletes: %{_lib}fontenc1-static-devel
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticdevelname}
Static development files for %{name}

%files -n %{staticdevelname}
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
