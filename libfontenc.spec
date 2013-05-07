%define major 1
%define libname %mklibname fontenc %{major}
%define develname %mklibname fontenc -d

Name:		libfontenc
Summary:	The fontenc Library
Version:	1.1.2
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libfontenc-%{version}.tar.bz2

BuildRequires:	zlib-devel
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
# list of encodings
Requires:	x11-font-encodings
Patch0:		libfontenc-aarch64.patch

%description
libfontenc is a library which helps font libraries portably determine and 
deal with different encodings of fonts.

%package -n %{libname}
Summary:	The fontenc Library
Group:		System/Libraries
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libfontenc is a library which helps font libraries portably determine and 
deal with different encodings of fonts.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libfontenc-devel = %{version}-%{release}
Obsoletes:	%{_lib}fontenc1-devel < 1.1.1
Obsoletes:	%{_lib}fontenc-static-devel < 1.1.1.
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}.

%prep
%setup -qn libfontenc-%{version}
%patch0 -p1

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir} \
	--with-encodingsdir=%{_datadir}/fonts/encodings

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libfontenc.so.%{major}*

%files -n %{develname}
%{_libdir}/libfontenc.so
%{_libdir}/pkgconfig/fontenc.pc
%{_includedir}/X11/fonts/fontenc.h

%changelog
* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-2
+ Revision: 783365
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Mon Mar 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-1
+ Revision: 782149
- version update  1.1.1

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.0-3
+ Revision: 745615
- rebuild
- disabled static build
- removed .la files
- cleaned up spec

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2
+ Revision: 660249
- mass rebuild

* Thu Oct 21 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 587077
- new release

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.5-1mdv2010.1
+ Revision: 463689
- New version: 1.0.5

* Wed Aug 26 2009 Emmanuel Andry <eandry@mandriva.org> 1.0.4-6mdv2010.0
+ Revision: 421586
- apply libraries policy

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-5mdv2009.0
+ Revision: 222558
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-4mdv2008.1
+ Revision: 152807
- Update BuildRequires and rebuild.
  Also disable patch1 as it is used only to "document" functions called
  by the X Server.

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-3mdv2008.1
+ Revision: 150559
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Fix typo. Almost calibrated to start changing the real packages.
    - This is a "noop" patch. But it can be considered a list of the functions,
      code from X Server uses from libfontenc, at a later stage, this library can be
      changed to make available only the public symbols.


* Fri Feb 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.4-1mdv2007.0
+ Revision: 121704
- new release

* Fri Nov 17 2006 Pablo Saratxaga <pablo@mandriva.com> 1.0.2-3mdv2007.1
+ Revision: 85159
- depend on x11-font-encodings
- fixed path for encodings.dir file

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

