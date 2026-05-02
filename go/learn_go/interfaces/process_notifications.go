package main

type notification interface {
	importance() int
}

type directMessage struct {
	senderUsername string
	messageContent string
	priorityLevel  int
	isUrgent       bool
}

type groupMessage struct {
	groupName      string
	messageContent string
	priorityLevel  int
}

type systemAlert struct {
	alertCode      string
	messageContent string
}

func (d directMessage) importance() (importanceScore int) {
	if d.isUrgent {
		importanceScore = 50
		return
	} else {
		importanceScore = d.priorityLevel
		return
	}
}

func (g groupMessage) importance() (importanceScore int) {
	importanceScore = g.priorityLevel
	return
}

func (s systemAlert) importance() (importanceScore int) {
	importanceScore = 100
	return
}

func processNotification(n notification) (string, int) {
	switch t := n.(type) {
	case directMessage:
		return t.senderUsername, t.importance()
	case groupMessage:
		return t.groupName, t.importance()
	case systemAlert:
		return t.alertCode, t.importance()
	default:
		return "", 0
	}
}
