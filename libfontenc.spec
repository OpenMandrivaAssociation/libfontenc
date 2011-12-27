%define major 1
%define libname %mklibname fontenc %{major}
%define develname %mklibname fontenc -d

Name: libfontenc
Summary:  The fontenc Library
Version: 1.1.0
Release: 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libfontenc-%{version}.tar.bz2

BuildRequires: zlib-devel
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
# list of encodings
Requires: x11-font-encodings

%description
libfontenc is a library which helps font libraries portably determine and 
deal with different encodings of fonts.

%package -n %{libname}
Summary:  The fontenc Library
Group: System/Libraries
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
libfontenc is a library which helps font libraries portably determine and 
deal with different encodings of fonts.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libfontenc-devel = %{version}-%{release}
Obsoletes: %{_lib}fontenc1-devel
Obsoletes: %{_lib}fontenc-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libfontenc-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir} \
	--with-encodingsdir=%{_datadir}/fonts/encodings

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libname}
%{_libdir}/libfontenc.so.%{major}*

%files -n %{develname}
%{_libdir}/libfontenc.so
%{_libdir}/pkgconfig/fontenc.pc
%{_includedir}/X11/fonts/fontenc.h

