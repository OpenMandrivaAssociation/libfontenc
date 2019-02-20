%define major 1
%define libname %mklibname fontenc %{major}
%define devname %mklibname fontenc -d
%define _disable_rebuild_configure 1

Summary:	The fontenc Library
Name:		libfontenc
Version:	1.1.4
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libfontenc-%{version}.tar.bz2

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(zlib)
# list of encodings
Requires:	x11-font-encodings

%description
libfontenc is a library which helps font libraries portably determine and 
deal with different encodings of fonts.

%package -n %{libname}
Summary:	The fontenc Library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libfontenc is a library which helps font libraries portably determine and 
deal with different encodings of fonts.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}fontenc1-devel < 1.1.1
Obsoletes:	%{_lib}fontenc-static-devel < 1.1.1.

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir} \
	--with-encodingsdir=%{_datadir}/fonts/encodings

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libfontenc.so.%{major}*

%files -n %{devname}
%{_libdir}/libfontenc.so
%{_libdir}/pkgconfig/fontenc.pc
%{_includedir}/X11/fonts/fontenc.h
