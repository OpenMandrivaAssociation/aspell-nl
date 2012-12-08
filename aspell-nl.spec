%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-2
%define fname aspell-%{languagecode}
%define aspell_ver 0.60
%define languagelocal nederlandse
%define languageeng dutch
%define languageenglazy Dutch
%define languagecode nl
%define lc_ctype ln_NL

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.2
Release:	%mkrel 19
Group:		System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides: spell-nl

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary

# RedHat Stuff. is this right:
#Obsoletes: ispell-fr, ispell-french

Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
./configure
%make

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# fix doc perms
chmod 644 README doc/*

cd $RPM_BUILD_ROOT%{_libdir}/aspell && ln -s nl.rws nederlands

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-19mdv2011.0
+ Revision: 662856
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-18mdv2011.0
+ Revision: 603448
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-17mdv2010.1
+ Revision: 518949
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-16mdv2010.0
+ Revision: 413091
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.50.2-15mdv2009.1
+ Revision: 350081
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-14mdv2009.0
+ Revision: 220433
- rebuild

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-13mdv2008.1
+ Revision: 190010
- remove 380k of docs from livecd

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.50.2-12mdv2008.1
+ Revision: 182506
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-11mdv2008.1
+ Revision: 148836
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-10mdv2007.0
+ Revision: 123339
- Import aspell-nl

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-10mdv2007.1
- use the mkrel macro
- disable debug packages

* Tue Oct 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.50.2-9mdk
- should not be a noarch packag

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-8mdk
- rebuild for new aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-7mdk
- allow build on ia64

