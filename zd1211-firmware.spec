%define name zd1211-firmware
%define version 1.4
%define release 15

Summary: Firmware files for the ZD1211 chip
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/zd1211/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://sourceforge.net/projects/zd1211/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This package contains the firmware files for the ZD1211 chip, which is
used in WLAN USB sticks.
The files are generated from C header files distributed in the
original ZyDAS ZD1211 driver under the GNU Public License.
The full source of the original ZYDAS driver is available from
http://www.deine-taler.de/zd1211/

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/zd1211
install -m644 zd1211* $RPM_BUILD_ROOT/lib/firmware/zd1211

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/lib/firmware/zd1211/zd1211*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-5mdv2011.0
+ Revision: 671954
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-4mdv2011.0
+ Revision: 608283
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-3mdv2010.1
+ Revision: 524479
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.4-2mdv2009.1
+ Revision: 350728
- rebuild

* Sun Mar 02 2008 Olivier Blin <oblin@mandriva.com> 1.4-1mdv2008.1
+ Revision: 177655
- 1.4 (from SourceForge, sync to vendor driver v2.21.0.0)
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2008.1
+ Revision: 130712
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - Import zd1211-firmware



* Tue Sep  5 2006 Olivier Blin <blino@mandriva.com> 1.1-2mdv2007.0
- install firmwares in /lib/firmware/zd1211

* Mon Jul 10 2006 Olivier Blin <blino@mandriva.com> 1.1-1mdv2007.0
- initial Mandriva release
