# Get Delegate User
from steem.account import Account
from openpyxl import load_workbook, Workbook

def run():
    print("랜딩 참여자 갱신을 시작합니다.")
    print("스팀 블록체인에서 데이터를 다운받고 있습니다.")
    userId = 'virus707'
    wb = Workbook()
    ws = wb.active
    accounts = {}
    for h in Account(userId).history_reverse(filter_by="delegate_vesting_shares"):
        if h['delegator'] not in accounts:
            vest = float(h['vesting_shares'][:-6])
            accounts[h['delegator']] = {}
            accounts[h['delegator']]['vest'] = vest
            accounts[h['delegator']]['date'] = h['timestamp']
    ws.append(["acocunt","timestamp","vests"])
    for k,v in accounts.items():
        if v['vest'] != 0.0:
            ws.append([k, v['date'], v['vest']])
    wb.save('accounts.xlsx')

    input("랜딩 참여자 갱신이 완료되었습니다. accounts.xlsx를 확인 바랍니다.")

if __name__ == "__main__":
    run()