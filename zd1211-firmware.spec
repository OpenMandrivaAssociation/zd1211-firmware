%define name zd1211-firmware
%define version 1.4
%define release %mkrel 4

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
